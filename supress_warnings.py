import warnings
#warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
warnings.filterwarnings("ignore", category=FutureWarning, module='folium.utilities')