from rest_framework import serializers
from .models import Producto

# model= Producto indica que modelo se transformara y validara
# fields= '__all__'exponde todos los campos del modelo
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields= '__all__'

    def validate_precio(self, value):
        if value <=0:
            raise serializers.ValidationError(
                'El precio debe ser mayor que cero.'
            )
        return value

    def validate_stock(self, value):
            if value <0:
                raise serializers.ValidationError(
                    'El stock no debe ser negativo.'
                )
            return value
    
    
