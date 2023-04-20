from odoo.tests import common


class TestEstateProperty(common.TransactionCase):
    def setUp(self):
        super(TestEstateProperty, self).setUp()
        self.EstateProperty = self.env["estate.property"]

    def test_create_estate_property(self):
        """Test creating a new estate property record."""
        # Prepare test data
        estate_property_data = {
            "name": "Test Estate Property",
            "bedrooms": 2,
            "state": "new",
            "date_availability": "2023-07-17",
            "expected_price": 100000,
        }

        # Create a new estate property record
        new_estate_property = self.EstateProperty.create(estate_property_data)

        # Check if the new estate property record was created successfully
        self.assertTrue(new_estate_property, "Estate property record was not created.")
        self.assertEqual(
            new_estate_property.name,
            "Test Estate Property",
            "Estate property name does not match the expected value.",
        )