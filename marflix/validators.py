import os
from django.core.exceptions import ValidationError

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = [
        '.3g2',
        '.3gp',
        '.aaf',
        '.asf',
        '.avchd',
        '.avi',
        '.drc',
        '.flv',
        '.m2v',
        '.m3u8',
        '.m4p',
        '.m4v',
        '.mkv',
        '.mng',
        '.mov',
        '.mp2',
        '.mp4',
        '.mpe',
        '.mpeg',
        '.mpg',
        '.mpv',
        '.mxf',
        '.nsv',
        '.ogg',
        '.ogv',
        '.qt',
        '.rm',
        '.rmvb',
        '.roq',
        '.svi',
        '.vob',
        '.webm',
        '.wmv',
        '.yuv'
    ]

    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão de arquivo inválida.')
    