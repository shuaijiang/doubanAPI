#!/usr/bin/python
#coding: utf-8
import urllib2
import time

fp_id = open('movie.id','r')
for movie_id in fp_id:
        movie_id=movie_id.replace('\n','')
        
        movie_file = './movie_information/' + movie_id + '.info'
        fp = open(movie_file,'w')

				#if you have a key, you can access 40 times per minute
				#then you can sleep less, you can sleep(1.6) for example
        url = 'http://api.douban.com/v2/movie/subject/'+ movie_id #+ '?apikey={apikey}'
        print url
        
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        html = res.read()
        fp.write(html)     
        res.close
        time.sleep(6)
        fp.close()
fp_id.close()
