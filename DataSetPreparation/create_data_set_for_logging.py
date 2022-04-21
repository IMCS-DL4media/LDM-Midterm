import os 
import shutil

#pienemam , ka root_dir_path satur n direktorijas, 
# katra direktorija atbilst vienai klasei
# si direktorija (kas atbilst klasei) satur tikai failus - ieklautas direktorijas netiek apstradatas
def create_index_file(root_dir_path, index_file_path):
    f = open(index_file_path, "w")
    for fpath in os.listdir(root_dir_path):
        print(fpath)
        if os.path.isdir(os.path.join(root_dir_path, fpath)):            
            for file in os.listdir( os.path.join(root_dir_path, fpath) ):
                print(file)
                if os.path.isfile( os.path.join(root_dir_path, fpath, file) ):
                    f.write(file +  " , " + fpath + "\n")
                    #f.write("\r\n")        
    f.close()


def create_dir_with_training_files(src_dir, dest_dir):
    if not os.path.isdir(src_dir) or not os.path.exists(src_dir):
        print("Directory " + src_dir + " not found.")
        return
    
    if not os.path.isdir(dest_dir) or not os.path.exists(dest_dir):
        #create dir
        print("Creating directory " + dest_dir)
        os.mkdir(dest_dir)

    for fpath in os.listdir(src_dir):
            print(fpath)
            if os.path.isdir(os.path.join(src_dir, fpath)):
                for file in os.listdir( os.path.join(src_dir, fpath) ):
                    print("\t" + file)
                    if os.path.isfile( os.path.join(src_dir, fpath, file) ):
                        #f.write(file +  " , " + fpath + "\n")
                        shutil.copyfile( os.path.join(src_dir, fpath, file), os.path.join(dest_dir, file))
                        #f.write("\r\n")

def create_dir_with_training_testing_files(src_dir, train_dest_dir, test_dest_dir):
    if not os.path.isdir(src_dir) or not os.path.exists(src_dir):
        print("Directory " + src_dir + " not found.")
        return
    
    if not os.path.isdir(train_dest_dir) or not os.path.exists(train_dest_dir):
        #create dir
        print("Creating directory " + train_dest_dir)
        os.mkdir(train_dest_dir)

    if not os.path.isdir(test_dest_dir) or not os.path.exists(test_dest_dir):
        #create dir
        print("Creating directory " + test_dest_dir)
        os.mkdir(test_dest_dir)

    train_ind = open( os.path.join(train_dest_dir , "labels.txt") , "w")
    test_ind  = open( os.path.join(test_dest_dir , "labels.txt"), "w")

    for fpath in os.listdir(src_dir):
            print(fpath)
            file_count = 0
            if os.path.isdir(os.path.join(src_dir, fpath)):
                for file in os.listdir( os.path.join(src_dir, fpath) ):
                    #print("\t" + file)
                    if os.path.isfile( os.path.join(src_dir, fpath, file) ):
                        file_count = file_count + 1
                        #f.write(file +  " , " + fpath + "\n")
                        #shutil.copyfile( os.path.join(src_dir, fpath, file), os.path.join(dest_dir, file))
                        #f.write("\r\n")
                print(file_count)

                #pirmos 80% no failiem liekam ieks train; parejo ieks test
                num_of_procesed_files = 0
                
                for file in os.listdir( os.path.join(src_dir, fpath) ):
                    #print("\t" + file)
                    if os.path.isfile( os.path.join(src_dir, fpath, file) ):
                        num_of_procesed_files = num_of_procesed_files + 1
                        if num_of_procesed_files < file_count * 0.8:
                            shutil.copyfile( os.path.join(src_dir, fpath, file), os.path.join(train_dest_dir, file))
                            train_ind.write(file +  " , " + fpath + "\n")
                        else:
                            shutil.copyfile( os.path.join(src_dir, fpath, file), os.path.join(test_dest_dir, file))
                            test_ind.write(file +  " , " + fpath + "\n")
                        #f.write(file +  " , " + fpath + "\n")
                        #shutil.copyfile( os.path.join(src_dir, fpath, file), os.path.join(dest_dir, file))
                        #f.write("\r\n")





def main():
    print("main")
    #create_dir_with_training_files("./kFineTuning-master/flowers17/", "./flowers17")
    #create_index_file("./kFineTuning-master/flowers17/", "./flowers17/index.txt")

    create_dir_with_training_testing_files("./kFineTuning-master/flowers17/", "./flowers17_train", "./flowers17_test")
    


main()