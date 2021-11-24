import math
from typing import Dict


def get_pagination_parameters(
        page_id: int, page_size: int, items_count: int, total_items_count: int
) -> Dict:
    """
    Solves the pagination parameter for a sub-collection of items

    :param page_id: The current page.
    :param page_size: The size of the page.
    :param items_count: Current items count.
    :param total_items_count: Total items count.

    :return: Pagination dictionary.
    """

    pagination = {
        "page_id": page_id,
        "page_size": page_size,
        "prev_page_id": None,
        "next_page_id": None,
        "items_on_page": items_count,
        "total_items": total_items_count,
    }

    total_pages = int(math.ceil(total_items_count / page_size))

    if 0 < page_id <= total_pages:
        pagination["prev_page_id"] = page_id - 1

    if page_id < total_pages - 1:
        pagination["next_page_id"] = page_id + 1

    return pagination
