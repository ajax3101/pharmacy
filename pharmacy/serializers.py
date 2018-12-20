from rest_framework import serializers
from pharmacy.models import Pharmacy, Drug


class PharmacySerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, pharmacy):
        request = self.context.get('request')
        logo_url = pharmacy.logo.url
        return request.build_absolute_uri(logo_url)
    class Meta:
        model = Pharmacy
        fields = ('id', 'name', 'phone', 'address', 'logo')

class DrugSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, drug):
        request = self.context.get('request')
        image_url = drug.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Drug
        fields = ('id', 'name', 'short_descr', 'image', 'price_sell')
