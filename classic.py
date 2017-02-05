class Command(BaseCommand):
    def handle(self, *args, **options):
        # compute cut off time
        utcnow = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
        cut_start = (utcnow + timedelta(hours=-12)).strftime('%Y-%m-%d %H:%M+00:00')
        cut_end = (utcnow + timedelta(hours=12)).strftime('%Y-%m-%d %H:%M+00:00')

        logger.debug('utc:%s, cut_start:%s, cut_end:%s' % (utcnow, cut_start, cut_end))

        # make sure target_datetime is UTC
        tasks = PushTask.objects.filter(target_datetime__range=(cut_start, cut_end), removed=False)
        logger.debug('Tasks to run: %s' % tasks.count())
        for task in tasks:
            logger.debug('Task id: %s' % task.id)
            target_timezone = int(((task.target_datetime - utcnow.replace(tzinfo=utc)).total_seconds())/3600)

            device_query = Q(device__user__isnull=True, time_zone=target_timezone, device__active=True)
            lsuser_query = Q(time_zone=target_timezone, alert_mobile_newsletter=1)

            #this is TEST switch
            # print "task_istest----->"
            if(task.istest):
                # print "this is a test"
                lsuser_query = lsuser_query & Q(user_id__in=[1,2,5,2213, 16370,16373,17438,26088,28360])
                #lsuser_query = lsuser_query & Q(user_id__in=[16370])

            #filter country
            if task.target_countries:
                targetcountries = task.target_countries.split(";")
                device_query = device_query & Q(rcountry__in=targetcountries)
                lsuser_query = lsuser_query & Q(rcountry__in=targetcountries)

            #filter languages
            r_msg = {"title":task.title,"subtitle":task.subtitle, "body":task.content}
            r_extra = {"typ":task.typ,"target" : task.link}
            r_msg_zh = {"title":task.title_zh,"subtitle":task.subtitle_zh, "body":task.content_zh}
            r_extra_zh = {"typ":task.typ,"target" : task.link_zh}

            # if already pushed to current timezone, skip
            if ';%s:' % target_timezone in task.sent_counts:
                continue

            total_sent = 0
            total_failed = 0
            if 'en' in task.target_languages:
                print "test-en"
                device_query_en = device_query & ~Q(language__in=['zh'])
                lsuser_query_en = lsuser_query & ~Q(language__in=['zh'])

                device_ids = DeviceExt.objects.filter(device_query_en).values_list('device_id', flat=True)
                user_ids = LSUser.objects.filter(lsuser_query_en).values_list('user_id', flat=True)

                #for test
                device_ids = []
                sent = 0
                failed = 0
                try:
                    (sent, failed) = noticehelper.pushNoticeByTimeZone(user_ids, device_ids, r_msg, r_extra)
                except Exception as ex:
                    logger.debug(str(ex))

                print "----------------"
                print "en:%s:%s" % (sent, failed)
                print "----------------"

                total_sent += sent
                total_failed += failed

            if 'zh' in task.target_languages:
                print "test-zh"
                device_query_zh = device_query & Q(language__in=['zh'])
                lsuser_query_zh = lsuser_query & Q(language__in=['zh'])

                device_ids = DeviceExt.objects.filter(device_query_zh).values_list('device_id', flat=True)
                user_ids = LSUser.objects.filter(lsuser_query_zh).values_list('user_id', flat=True)
                # print device_ids, user_ids

                #for test
                device_ids = []
                sent = 0
                failed = 0
                try:
                    (sent, failed) = noticehelper.pushNoticeByTimeZone(user_ids, device_ids, r_msg_zh, r_extra_zh)
                except Exception as ex:
                    logger.debug(str(ex))

                print "----------------"
                print "zh:%s:%s" % (sent, failed)
                print "----------------"

                total_sent += sent
                total_failed += failed

            task.sent_counts = '%s;%s:%s|%s' % (task.sent_counts, target_timezone, total_sent, total_failed)
            print task.sent_counts

            task.save()
