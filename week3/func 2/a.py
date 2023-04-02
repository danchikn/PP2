movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def scgreat(movie):
        if(movie['imdb']>5.5):
            return True
        else:
            return False
check=scgreat(movies[2])
if(check):
    print('True')
else :
    print ('False')
    
print(None)


#2
def high(movies):
    oulist=[];
    for i in range(0,len(movies)):
        allmov=movies[i];
        if allmov['imdb']>5.5:
            oulist.append(allmov)
    return oulist
oulist = high(movies)
print(oulist)

print(None)


#3
def movcategory(movies,name): 
        oulist=[]
        for i in movies:
            current=i['category']
            if name.lower()==current.lower():
                oulist.append(i)
        return oulist
oulist = movcategory(movies, 'Romance')
print(oulist)

print(None)




#4
def average_val(movies): 
        average=0
        top=len(movies)
        for i in movies:
            average=average+i['imdb']
        average=average/top
        return average
v = average_val(movies)
print(v)

print(None)




#5
def avg(movies,name):
        cat_movies=movcategory(movies,name)
        avg_score=average_val(cat_movies)
        return avg_score
v2=avg(movies,'Thriller')
print (v2)