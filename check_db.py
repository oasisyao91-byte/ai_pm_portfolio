import asyncio
from sqlalchemy import select, func
from app.db.session import AsyncSessionLocal
from app.models.sql_models import L2L3ClassifyResult, BatchJob

async def check():
    async with AsyncSessionLocal() as db:
        # Check jobs
        jobs = await db.execute(select(BatchJob).where(BatchJob.job_type == 'l2_classify').order_by(BatchJob.result_version))
        print("Jobs:")
        for job in jobs.scalars().all():
            print(f"Job {job.job_id}, Version {job.result_version}, Status {job.status}, Config {job.config}")

        # Check results for v7, v8
        for v in [7, 8]:
            count = await db.execute(select(func.count(L2L3ClassifyResult.id)).where(L2L3ClassifyResult.version == v))
            c = count.scalar()
            print(f"Version {v} count: {c}")
            
            if c > 0:
                # Show sample
                res = await db.execute(select(L2L3ClassifyResult).where(L2L3ClassifyResult.version == v).limit(1))
                r = res.scalar()
                print(f"Sample V{v}: L2={r.l2}, L3={r.l3}, Job={r.job_id}")

if __name__ == "__main__":
    asyncio.run(check())
