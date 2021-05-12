from datetime import datetime
from loguru import logger
from url_shortener import create_app
from url_shortener.models import db, Url


if __name__ == '__main__':
    app = create_app()
    logger.add('deletion.log', format="{time} {level} {message}", level="INFO", rotation="5 MB", compression="zip")

    with app.app_context():
        urls = Url.query.filter(Url.valid_until < datetime.now()).all()
        logger.info('Starting a cleanup session: ')

        for url in urls:
            logger.info(f'Deleting {url}')

        num_rows_deleted = db.session.query(Url).filter(Url.valid_until < datetime.now()).delete()
        db.session.commit()

        logger.info(f'Deleted {num_rows_deleted} records.')
