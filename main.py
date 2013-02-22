
import webapp2
import json
import detect
import random

class MainHandler(webapp2.RequestHandler):

    def process_query(self, query):
        ## do something with the query
        result = detect.process(query)

        return json.dumps(result)

    def chart(self, query):        
        result = detect.process(query)

        airlines = {}
        for row in result:
            airline = row[4]
            if airline not in airlines:
                airlines[airline] = 0
            airlines[airline] += 1

        out = {
            'name': 'airports',
            'children': []
        }

        for airline in airlines:
            group = {
                'name': 'flights-for-' + airline,
                'children': [
                    { 'name': airline, 'size': 100*airlines[airline]/len(result) }
                ]
            }
            out['children'].append(group)

        return json.dumps(out)

    def chart_large(self, query):        
        result = detect.process(query)

        out = 'price,price2,airline\n'
        for row in result:
            out += row[3] + ',' + str(float(row[3]) + random.random()*250) + ',' + row[4] + '\n'

        return out

    def get(self):
        query = self.request.get('q')
        m = self.request.get('m')
        
        result = ''
        if m == 'chart':
            result = self.chart(query)        
        elif m == 'chart-large':
            result = self.chart_large(query)
        else:
            result = self.process_query(query)
            self.response.headers['Content-Type'] = 'application/json'
        

        self.response.write(result)


app = webapp2.WSGIApplication([
    ('/api', MainHandler)
], debug=True)
