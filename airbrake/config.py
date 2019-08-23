import airbrake


logger = airbrake.getLogger(api_key="3ee9d6fc6b462f0dae3b37a41366e914", project_id=237813)

try:
    1/0
except Exception:
    logger.exception("Bad math.")
