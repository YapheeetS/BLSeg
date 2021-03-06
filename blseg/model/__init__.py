from .fcn import FCN
from .unet import UNet, ModernUNet
from .pspnet import PSPNet
from .deeplab import DeepLabV3Plus
from .gcn import GCN

__all__ = [
    "FCN",
    "UNet",
    "ModernUNet",
    "PSPNet",
    "DeepLabV3Plus",
    "GCN",
]
