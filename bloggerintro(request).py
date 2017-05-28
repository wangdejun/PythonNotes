def bloggerintro(request):
    lsuser = authhelper.getlsuser(request)
    query = Q(removed=False, commission__gt=0) & (Q(lssupport=True) | Q(cjsupport=True))
    merchants = Merchant.objects.filter(query).order_by('-epc')

    result = []
    for merchant in merchants:
        tmp = {
            'name': merchant.name,
            'website': merchant.website,
            'commission': merchant.commission,
            'murl': merchant.geturl(),
            'epc': merchant.epc,
            'logo': merchant.logo
        }

        result.append(tmp)
        print tmp

    template_values = {
        'frame': 'frame.html',
        'lsuser': lsuser,
        'migrated': 1,
        'merchants': result
    }

    response = render(request, 'reward/bloggerintro.html', template_values)

    return response