import json 

input_file=r'C:\Users\parikshit\Downloads\Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json'
prefix='split_file'
num_files=10



with open(input_file,'r',encoding="utf8") as f:
    total_num=sum(1 for _ in f)

print(total_num)

lines_per_file=total_num // num_files
 # print(lines_per_file)


with open(input_file,'r',encoding='utf8') as f:
    for i in range(num_files):
        output_filename= f"{prefix}{i+1}.json"
        # print(i)

        with open(output_filename,'w',encoding='utf8') as out_file:
            for j in range(lines_per_file):
                line=f.readline()
                if not line:
                    break
                out_file.write(line)



