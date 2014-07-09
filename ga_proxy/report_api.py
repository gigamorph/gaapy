class ReportAPI(object):

    def __init__(self, service):
        self.service = service

    def get_report(self, params):
        return self.service.data().ga().get(
            ids='ga:' + params['profile_id'],
            start_date=params['start'],
            end_date=params['end'],
            filters=params.get('filters'),
            dimensions=params.get('dimensions'),
            metrics=params.get('metrics')).execute()
