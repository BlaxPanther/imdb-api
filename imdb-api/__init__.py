import requests
from bs4 import BeautifulSoup
import json
import re

class IMDb:
    
    url="https://www.imdb.com"
    
    def getIdFromSearch(self,search):
        if search == "":
            return ""
        if re.match(r"^tt\d{7,}$", search):
            return search
        source = IMDb.getPage(IMDb.url+"/find?q="+search)
        if source != "":
            if "No results found" in source.text:
                print("No title match found.")
                return ""
            try:
                result = source.find('td',{'class':'result_text'}).a        
                return result["href"].split("/")[2]
            except:
                print("An error occured. Please report this issue (error_code=1) or wait for the next update.")
                return ""  
            


    def getTitle(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["name"]
        except:
            return ""

    def getReleaseYear(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["props"]["pageProps"]["aboveTheFoldData"]["releaseYear"]["year"]
        except:
            return ""
    
    def getDirector(self, imdb_id, details = None, InList = False, name_id = False):
        return IMDb.getPeople(self, imdb_id, people_type="director", details = details, InList = InList, name_id = name_id)
    
    def getCreator(self, imdb_id, details = None, InList = False, name_id = False):
        return IMDb.getPeople(self, imdb_id, people_type="creator", details = details, InList = InList, name_id = name_id)
    
    def getMainActors(self, imdb_id, details = None, InList = True, name_id = False):
        return IMDb.getPeople(self, imdb_id, people_type="actor", details = details, InList = InList, name_id = name_id)    
    
    def getPeople(self, imdb_id, people_type, details = None, InList = False, name_id = False):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            People = []            
            people_details = details[people_type]            
            for person in people_details:
                if "name" in person:
                    if name_id:
                        person_to_add = {}
                        person_to_add[people_type] = person["name"]
                        person_to_add["id"] = person["url"][6:-1]
                        People.append(person_to_add)
                    else:
                        People.append(person["name"])
            if InList or name_id:
                return People
            else:
                return IMDb.ListToText(People)
        except:
            if InList:
                return []
            else:
                return ""    
    
    def getCountries(self, imdb_id, source = None):
        return IMDb.getInfo(self, imdb_id, "country", source = source)
    
    def getLanguages(self, imdb_id, source = None):
        return IMDb.getInfo(self, imdb_id, "language", source = source)
                         
    def getCompanies(self, imdb_id, source = None):
        return IMDb.getInfo(self, imdb_id, "company", source = source)
    
    def getInfo(self, imdb_id, info_type, source = None, InList = True):
        if info_type == "language":
            info_id = "title-details-languages"
        elif info_type == "country":
            info_id = "title-details-origin"
        elif info_type == "company":
            info_id = "title-details-companies"
        elif info_type == "aka":
            info_id = "title-details-akas"
        elif info_type == "filming_location":
            info_id = "title-details-filminglocations"
        else:
            print("Invalid argument in getInfo")
            return ""
        info = []
        try:
            imdb_id = IMDb.getIdFromSearch(self, imdb_id)
            if source is None:
                source = IMDb.getPage(IMDb.url+"/title/"+imdb_id)
            li = source.find("li",{"data-testid":info_id})
            div = li.find("div",{"class":"ipc-metadata-list-item__content-container"})
            for a in div.find_all("a"):
                info.append(a.text)
            if len(info) == 0:
                for a in div.find_all("span"):
                    info.append(a.text)            
            if InList:
                return info
            else:
                return IMDb.ListToText(info)
        except:
            if InList:
                return []
            else:
                return ""    
    
    
    def getGenres(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["genre"]
        except:
            return ""
    
    def getType(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["@type"]
        except:
            return ""
        
    def getRuntime(self, imdb_id, details = None, seconds = False):
        try:
            details = IMDb.getDetails(self, imdb_id, details)     
            if seconds:
                duration = details["props"]["pageProps"]["aboveTheFoldData"]["runtime"]["seconds"]
            else:
                duration_raw = details["duration"][2:-1]
                if "H" not in duration_raw:
                    if len(duration_raw) == 1:
                        duration_raw = "0" + duration_raw
                    duration = "0h"+duration_raw
                else:
                    if len(duration_raw) == 3:
                        duration = duration_raw.replace("H","h0")
                    else:
                        duration = duration_raw.replace("H","h")
            return duration
        except:
            return ""

    def getReleaseDate(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)   
            if "datePublished" in details:
                return details["datePublished"] 
            else:
                 release_date = details["props"]["pageProps"]["aboveTheFoldData"]["releaseDate"]
                 if release_date["year"] is not None:
                     date = str(release_date["year"])
                     if release_date["month"] is not None:
                         month=str(release_date["month"])
                         if len(month) == 1:
                             month = "0" + month
                         date += "-"+month           
                         if release_date["day"] is not None:
                             day = str(release_date["day"])
                             if len(day) == 1:
                                 day = "0" + day
                             date += "-"+day 
            return date
        except:
            return ""           

    def getDescription(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["description"]
        except:
            return ""
        
    def getContentRating(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["contentRating"]
        except:
            return ""

    def getRating(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["aggregateRating"]["ratingValue"]
        except:
            return ""
    
    def getRatingCount(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["aggregateRating"]["ratingCount"]
        except:
            return ""
        
    def getReviewsCount(self, imdb_id, source = None): 
        try:
            imdb_id = IMDb.getIdFromSearch(self, imdb_id)
            if source is None:
                source = IMDb.getPage(IMDb.url+"/title/"+imdb_id)
            div = source.find("div",{"data-testid":"reviews-header"})
            reviews_count = div.find("span",{"class":"ipc-title__subtext"}).text
            if "K" in reviews_count:
                int_reviews_count = int(float(reviews_count[:-1])*1000)
            else:
                int_reviews_count = int(reviews_count)
            return int_reviews_count
        except:
            return 0
    
    def getFeatures(self, imdb_id, seconds = False, InList = False, name_id = False):
        features = {}
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        source = IMDb.getPage(IMDb.getURL(imdb_id))
        details = IMDb.getDetails(self, imdb_id, source = source)
        if details != "":
            features["title"] = IMDb.getTitle(self, imdb_id, details)
            features["release_year"] = IMDb.getReleaseYear(self, imdb_id, details)
            features["imdb_id"] = imdb_id            
            features["director"] = IMDb.getDirector(self, imdb_id, details, InList, name_id)
            features["creator"] = IMDb.getCreator(self, imdb_id, details, InList, name_id)
            features["main_actors"] = IMDb.getMainActors(self, imdb_id, details, InList = True, name_id = name_id)
            features["countries"] = IMDb.getCountries(self, imdb_id, source)
            features["languages"] = IMDb.getLanguages(self, imdb_id, source)
            features["companies"] = IMDb.getCompanies(self, imdb_id, source)            
            features["genre"] = IMDb.getGenres(self, imdb_id, details)
            features["type"] = IMDb.getType(self, imdb_id, details)
            features["runtime"] = IMDb.getRuntime(self, imdb_id, details, seconds)  
            features["release_date"] = IMDb.getReleaseDate(self, imdb_id, details)
            features["description"] = IMDb.getDescription(self, imdb_id, details)
            features["content_rating"] = IMDb.getContentRating(self, imdb_id, details)
            features["rating"] = IMDb.getRating(self, imdb_id, details)
            features["rating_count"] = IMDb.getRatingCount(self, imdb_id, details)
            features["reviews_count"] = IMDb.getReviewsCount(self, imdb_id, source)
        if features != {}:
            return features
        
    def getAllFeatures(self, imdb_id, seconds = False, InList = False, name_id = False):
        features = {}
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        source = IMDb.getPage(IMDb.getURL(imdb_id))
        details = IMDb.getDetails(self, imdb_id, source = source)
        if details != "":
            features["title"] = IMDb.getTitle(self, imdb_id, details)
            features["release_year"] = IMDb.getReleaseYear(self, imdb_id, details)
            features["imdb_id"] = imdb_id            
            features["director"] = IMDb.getDirector(self, imdb_id, details, InList, name_id)
            features["creator"] = IMDb.getCreator(self, imdb_id, details, InList, name_id)
            features["main_actors"] = IMDb.getMainActors(self, imdb_id, details, InList = True, name_id = name_id)
            features["countries"] = IMDb.getCountries(self, imdb_id, source)
            features["languages"] = IMDb.getLanguages(self, imdb_id, source)
            features["companies"] = IMDb.getCompanies(self, imdb_id, source)            
            features["genre"] = IMDb.getGenres(self, imdb_id, details)
            features["type"] = IMDb.getType(self, imdb_id, details)
            features["runtime"] = IMDb.getRuntime(self, imdb_id, details, seconds)  
            features["release_date"] = IMDb.getReleaseDate(self, imdb_id, details)
            features["description"] = IMDb.getDescription(self, imdb_id, details)
            features["content_rating"] = IMDb.getContentRating(self, imdb_id, details)
            features["rating"] = IMDb.getRating(self, imdb_id, details)
            features["rating_count"] = IMDb.getRatingCount(self, imdb_id, details)
            features["reviews_count"] = IMDb.getReviewsCount(self, imdb_id, source)
            features["keywords"] = IMDb.getKeywords(self, imdb_id, details, InList)
            features["filming_location"] = IMDb.getFilmingLocation(self, imdb_id, source, InList)
            features["aka"] = IMDb.getAka(self, imdb_id, source, InList)
            features["poster_url"] = IMDb.getPosterURL(self, imdb_id, details)
            features["trailer_url"] = IMDb.getTrailerURL(self, imdb_id, details)
            features["trailer_download_url"] = IMDb.getTrailerDownloadURL(self, imdb_id, details)
            features["trailer_thumbnail_url"] = IMDb.getTrailerThumbnailURL(self, imdb_id, details)    
        if features != {}:
            return features
    
    def getCast(self, imdb_id, limit = 15, uncredited = False, all = False, name_id = False):
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        if imdb_id == "":
            return []
        source_actors = IMDb.getPage(IMDb.url+"/title/"+imdb_id+"/fullcredits")
        cast_list = []
        if source_actors != "":
            full_cast = source_actors.find("table",{"class":"cast_list"})
        if full_cast is not None:
            counter = 0            
            for actor in full_cast.find_all('tr')[1:]:
                row_number = 0
                cast = {}
                for row in actor.find_all('td'):
                    if row_number == 1:
                        cast["actor"] = re.sub(r"[\t\r\n]","",row.text).strip()
                    if row_number == 3:
                        character = re.sub(r"[\t\r\n]","",row.text).strip() 
                        character = re.sub(r" +", " ", character)
                        if "uncredited" in character and not uncredited:
                            continue
                        cast["character"] = character
                        cast_list.append(cast)
                        counter += 1
                    if name_id:
                        if row_number == 0 and row.a is not None:
                            cast["id"] = row.a["href"][6:-1]
                    row_number += 1
                if counter == limit and not all:
                    break
        else:
            print("No actors found.")
        return cast_list  
    
    def getFeaturesWithCast(self, imdb_id, seconds = False, InList = False, limit = 15, uncredited = False, all = False, name_id = False):
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        features = IMDb.getFeatures(self, imdb_id, seconds, InList, name_id)
        if features is not None:
            features["cast"] = IMDb.getCast(self, imdb_id, limit, uncredited, all, name_id)
            return features
    
    def getAll(self, imdb_id, seconds = False, InList = False, limit = 15, uncredited = False, all = False, name_id = False):
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        features = IMDb.getAllFeatures(self, imdb_id, seconds, InList, name_id)
        if features is not None:
            features["cast"] = IMDb.getCast(self, imdb_id, limit, uncredited, all, name_id)
            return features
    
    def getPosterURL(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["image"]
        except:
            return "" 
        
    def getTrailerURL(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return IMDb.url+details["trailer"]["embedUrl"]
        except:
            return ""
        
    def getTrailerDownloadURL(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["props"]["pageProps"]["aboveTheFoldData"]["primaryVideos"]["edges"][0]["node"]["playbackURLs"][0]["url"]
        except:
            return ""
    
    def getTrailerThumbnailURL(self, imdb_id, details = None):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            return details["trailer"]["thumbnail"]["contentUrl"]
        except:
            return ""    
        
    def getMedia(self, imdb_id):
        media = {}
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        details = IMDb.getDetails(self, imdb_id)
        if details != "":
            media["title"] = IMDb.getTitle(self, imdb_id, details)
            media["release_year"] = IMDb.getReleaseYear(self, imdb_id, details)
            media["imdb_id"] = imdb_id
            media["poster_url"] = IMDb.getPosterURL(self, imdb_id, details)
            media["trailer_url"] = IMDb.getTrailerURL(self, imdb_id, details)
            media["trailer_download_url"] = IMDb.getTrailerDownloadURL(self, imdb_id, details)
            media["trailer_thumbnail_url"] = IMDb.getTrailerThumbnailURL(self, imdb_id, details)
        if media != {}:
            return media    
    
    def getKeywords(self, imdb_id, details = None, InList = True):
        try:
            details = IMDb.getDetails(self, imdb_id, details)
            if InList:
                return details["keywords"].split(",")
            else:
                return details["keywords"]
        except:
            return ""
        
    def getAka(self, imdb_id, source = None, InList = False):
        return IMDb.getInfo(self, imdb_id, "aka", source = source, InList = InList)
                
    def getFilmingLocation(self, imdb_id, source = None, InList = False):
        return IMDb.getInfo(self, imdb_id, "filming_location", source = source, InList = InList)
     
    def getDetails(self, imdb_id, details = None, source = None):
        if imdb_id == "":
            return ""
        imdb_id = IMDb.getIdFromSearch(self, imdb_id)
        if details is not None:
            return details
        else:
            if source is None:
                source = IMDb.getPage(IMDb.getURL(imdb_id))
            if source != "":
                # try:                
                details1 = source.find("script",type="application/ld+json")
                details1 = re.sub(r'<.*?{', '{',str(details1) )
                details1 = re.sub(r'</.*','',details1)
                details1 = IMDb.delDoubleQuotes(details1)
                details_json1 = json.loads(details1)
                details2 = source.find("script",type="application/json")
                details2 = re.sub(r'<.*?{', '{',str(details2) )
                details2 = re.sub(r'</.*','',details2)
                details_json2 = json.loads(details2)
                details_json = {}
                details_json.update(details_json1)
                details_json.update(details_json2)
                return details_json
                # except:
                #     print("An error occured. Please report this issue (error_code=2) or wait for the next update.")
                #     return ""
            else:
                return ""
            
            
    def delDoubleQuotes(json):
        double_quotes = []
        for i in range(len(json)):
            if json[i] == '"':
                if json[i-1] not in ["{",":","["] and json[i-2:i] not in ["],",'",','},']+[str(i)+"," for i in range(10)] and json[i+1] not in [":","}","]"] and json[i+1:i+3] not in [",[",',"',',{']:
                    double_quotes.append(i)
        i = len(double_quotes) - 1
        while i >= 0:
            json = json[:double_quotes[i]] + "''" + json[double_quotes[i]+1:]
            i -= 1
        return json

    def ListToText(List):
        text = ""
        if len(List) > 1:
            for item in List[:-1]:
                text += item + ", "
        text += List[-1]
        return text    

    def getURL(imdb_id):
        if re.match(r"^tt\d{7,}$", imdb_id):
            return IMDb.url+"/title/"+imdb_id
        else:
            return ""      

    def getPage(url):
        if url == "":
            return ""
        try:
            resp = requests.get(url)
            source = BeautifulSoup(resp.text.replace("&apos;","'").replace("&quot;",'"').replace("&gt;",">").replace( "&lt;","<").replace("&amp;","&"), "html5lib")
            return source
        except:
            print("A network error occured. Please, check your internet connection.")
            return ""
        


