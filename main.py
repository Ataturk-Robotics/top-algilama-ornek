import cv2 #scriptimize openc'yi ekliyoruz

ball_cascade = cv2.CascadeClassifier("frc2020-ball.xml")    #Topun haar cascade'ini
                                                            #ball_cascade değişkenine atıyoruz

while True:     #sonsuz bir döngü oluşturuyoruz

    frame = cv2.imread("IMG_2509-1.jpg")    #algılama yapacağımız resmi frame değişkenine atıyoruz

    if hasattr(frame,"size"):           #resim bulunduysa görüntü işlemeye başlıyoruz

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #resmi siyah beyaza çeviriyoruz

        balls = ball_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)
        #resimdeki topların listesini buluyoruz
        for (x,y,w,h) in balls:         #elde ettiğimiz listenin üyeleri, 
                                        #(x koordinatı, y koordinatı, x uzunluk, y yükseklik) şeklinde
            
            print(x,y,w,h) #(İSTEĞE BAĞLI) kooordinatları konsola yazdırıyoruz (güzel gözüksün diye)

            color = (255,0,0)       #Çerçeve rengi (BGR)
            thickness = 2           #Çerçeve kalınlığı (piksel)
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,thickness)#algılanan objenin entrafında mavi,
                                                                #2 piksellik çerçeve çiziyoruz
            
        cv2.imshow("frame",frame)   #(İSTEĞE BAĞLI) resmi ekrana çıkarıyoruz
    else:
        print("Resim yok ya da hatalı")  #resim bulunamadaıysa ya da hatalıysa konsola hata veriyoruz
    
    if cv2.waitKey(20) & 0xFF == ord("q"):  #q tuşuna basılınca sonsuz döngüden çıkıyoruz
        break
