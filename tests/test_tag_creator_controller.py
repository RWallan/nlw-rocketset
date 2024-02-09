from unittest.mock import patch

from nlw_rocketset.controllers.tag_creator_controller import (
    TagCreateController,
)
from nlw_rocketset.drivers.barcode_handler import BarcodeHandler


@patch.object(BarcodeHandler, "create_barcode")
def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreateController()

    result = tag_creator_controller.create(mock_value)

    assert result == {
        "data": {"type": "Tag Image", "count": 1, "path": f"{mock_value}.png"}
    }
