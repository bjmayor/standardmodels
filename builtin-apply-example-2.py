def function(a, b):
    print a,b

apply(function, ("crunchy", "frog"))
apply(function, ("crunchy",),{"b":"frog"})
apply(function, (),{"a":"crunchy","b":"frog"})
