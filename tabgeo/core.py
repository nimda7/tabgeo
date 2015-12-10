import os.path
from struct import unpack


ISO = ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ',
       'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS',
       'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN',
       'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE',
       'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF',
       'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM',
       'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM',
       'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC',
       'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK',
       'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA',
       'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG',
       'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW',
       'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS',
       'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO',
       'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI',
       'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW', 'XA', 'YU', 'CS', 'AN', 'AA', 'EU', 'AP',
       )


def split_str_fix(s, l):
    """ Split a string into chunks of length l """
    return [s[i:i+l] for i in range(0, len(s), l)]


def tabgeo_bs(data_array, ip, step):
    u = {}
    u_prev = {}
    start = 0
    end = len(data_array) - 1

    while True:
        mid = (start + end) // 2

        if step:
            (u['offset'], u['ip'], u['cc_id']) = unpack(">IBB", b'\x00'+data_array[mid])
        else:
            (u['ip'], u['cc_id']) = unpack(">BB", data_array[mid])
        if u['ip'] == ip:
            return u
        if end - start < 0:
            return u if ip > u['ip'] else u_prev
        if u['ip'] > ip:
            end = mid-1
        else:
            start = mid + 1

        u_prev = u


def getbyip(ip):
    ip_ = list(map(int, ip.split('.')))
    with open(os.path.join(os.path.dirname(__file__), 'data/tabgeo_country_v4.dat'), 'rb', 1) as fh:
        fh.seek((ip_[0]*256 + ip_[1])*4)
        index_bin = fh.read(4)
        (i_offset, i_length) = unpack(">IB", b'\x00'+index_bin)
        if i_offset == 16777215:
            return ISO[i_length]

        fh.seek(i_offset*5 + 262144)
        bin_data = fh.read((i_length+1)*5)
        d = tabgeo_bs(split_str_fix(bin_data, 5), ip_[2], True)
        if d['offset'] == 16777215:
            return ISO[d['cc_id']]

        if ip_[2] > d['ip']:
            ip_[3] = 255
        fh.seek(-((d['offset'] + 1 + d['cc_id']) * 2), 2)
        bin_data = fh.read((d['cc_id'] + 1) * 2)
        d = tabgeo_bs(split_str_fix(bin_data, 2), ip_[3], False)
        return ISO[d['cc_id']]

