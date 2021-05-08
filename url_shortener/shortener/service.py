from datetime import datetime, timedelta
from typing import Union
from ..models import db, Url
from ..utils import generate_short_string
from .dto import CreateNewLinkDto


def create_short_url(new_link: CreateNewLinkDto) -> str:
    is_already_present = Url.query.filter_by(original_url=new_link.original_url).first()

    if is_already_present:
        return is_already_present.short_url

    url = Url(
        original_url=new_link.original_url,
        short_url=generate_short_string(new_link.original_url),
        created_at=datetime.now(),
        days_to_expire=new_link.days_to_expire,
        valid_until=datetime.now() + timedelta(days=new_link.days_to_expire)
    )

    db.session.add(url)
    db.session.commit()

    return url.short_url


def view_original_url(short_url: str) -> Union[str, None]:
    url = Url.query.filter_by(short_url=short_url).first_or_404()

    if datetime.now() < url.valid_until:
        return url.original_url

    else:
        db.session.delete(url)
        db.session.commit()
