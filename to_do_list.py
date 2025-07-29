def  main (): 
    tasks = [] 

    while  True :
        print ( "\n===== Yapılacaklar Listesi =====" ) 
        print ( "1. Görev Ekle" ) 
        print ( "2. Görevleri Göster" ) 
        print ( "3. Görevi Tamamlandı Olarak İşaretle" ) 
        print ( "4. Çık" ) 

        choice = input ( "Seçiminizi girin: " ) 

        if choice == '1' : 
            print () 
            n_tasks = int ( input ( "Kaç görev eklemek istiyorsunuz: " )) 
            
            for i in  range (n_tasks): 
                task = input ( "Görevi girin: " ) 
                tasks.append({ "task" : task, "done" : False }) 
                print ( "Görev eklendi!" ) 

        elif choice == '2' : 
            print ( "\nGörevler:" ) 
            for index, task in  enumerate (tasks): 
                status = "Tamamlandı"  if task[ "done" ] else  "Tamamlanmadı" 
                print ( f" {index + 1 } . {task[ 'task' ]} - {status} " ) 

        elif choice == '3' : 
            task_index = int ( input ( "Tamamlandı olarak işaretlenecek görev numarasını girin: " )) - 1 
            if  0 <= task_index < len (tasks): 
                tasks[task_index][ "done" ] = True 
                print ( "Görev tamamlandı olarak işaretlendi!" ) 
            else : 
                print ( "Geçersiz görev numarası." ) 

        elif choice == '4' : 
            print ( "Yapılacaklar Listesinden Çıkılıyor." ) 
            break 

        else : 
            print ( "Geçersiz seçim.Lütfen tekrar deneyin." ) 

if __name__ == "__main__" : 
    main()