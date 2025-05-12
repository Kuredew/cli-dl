from . import logging

def is_audio(format):
    if format['audio_ext'] != 'none':
        return True
    
    return False

def find_audio_format(formats):
    abr_dic = {}

    if type(formats) is list:
        for idx, format in enumerate(formats):
            if format['audio_ext'] != 'none':
                abr = format['abr']

                if abr != None:
                    abr_dic[idx] = abr

        if abr_dic:
            larger_abr_format = max(abr_dic, key=abr_dic.get)
            format = formats[int(larger_abr_format)]

            return format
    
    logging.warn('Tidak menemukan Audio.')
    return False