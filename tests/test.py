# Visite esta página (https://tutosrivegamerlq.github.io/chromologger/)
# Visite esta página (https://tutosrivegamerlq.github.io/chromolog/)

# pip install chromologger
from chromologger import Logger 

log = Logger()

# Regsitro de error, con bloque try
try:
    # Soy literalmente un error
    tutosrivegamer
except Exception as e:
    log.log_e(e)