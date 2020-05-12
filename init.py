    import zipfly
    
    paths = [ 
        {
            'fs': 'home/user/Videos/jupiter.mp4', 
            'n': 'movies/jupiter.mp4', 
        },       
        {
            'fs': 'home/user/Documents/mercury.mp4', 
            'n': 'movies/mercury.mp4', 
        },          
    ]

    zfly = zipfly.ZipFly( paths = paths )

    generator = zfly.generator()
    print ( generator )
    # <generator object generator at 0x7f85aad60b13>

    with open("test.zip", "wb") as f:
        for i in generator:
            f.write(i)
