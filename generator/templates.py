gen_open = '''\
#include <stdlib.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

#include <uk/config.h>

int main() {
    int fd = {{ func_name }}({{ params }});
    
    if (fd < 0) {
        printf("Error opening file!\\n");     
        return -1;
    }
    
    close(fd);
    return 0;
}\
    '''


gen_isupper = '''\
#include <stdio.h>
#include <ctype.h>

#include <uk/config.h>

int main() {
    int a = {{ params }};
    printf("isupper(%d) = %d\\n", a, {{ func_name }}(a));
    
    return 0;
}\
'''


gen_malloc = '''\
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#include <uk/config.h>

int main() {
    int len = {{ params }};
    printf("For malloc function: len = %d\\n", len);
    char *mem = (char *){{ func_name }}(len);
    
    if (mem == NULL)
        fprintf(stderr, "failed to allocate memory.\\n");
    else {
        printf("memory allocated successfully\\n");
        free(mem);
    }
    
    return 0;
}\
'''


gen_memset = '''\
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <uk/config.h>

int main() {
    int str_len = 1024;
    char *str = (char *)malloc(str_len);
        
    {{ func_name }}(str, {{ params }}, str_len);
    
    printf("string is: %s\\n", str);
    
    return 0;
}\
'''


gen_strncpy = '''\
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <uk/config.h>

int main() {
    int str_len = 20, nums = {{ params }};
    char *src_str = (char *)malloc(str_len);
    char *dest_str = (char *)malloc(str_len);
    
    memset(src_str, 97, str_len);
    memset(dest_str, 98, str_len);
    
    printf("nums = %d\\n", nums);
    printf("src string is: %s\\n", src_str);
    printf("dest string is: %s\\n", dest_str);
    
    {{ func_name }}(dest_str, src_str, nums);
    
    printf("dest string is: %s\\n", dest_str);
    
    return 0;
}\
'''


gen_read = '''\
#include <unistd.h>
#include <stdio.h>
#include <uk/config.h>

int main()
{
    char data[128];
    
    if (read({{params}}, data, 128) < 0) {
        printf("An error occurred in the read.\\n");
        
        return -1;
    }
    
    printf("buffer is now: %s\\n", data);
        
    return 0;
}\
'''


gen_write = '''\
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
 
int main(void)
{
    // int fd = open("testfile.txt", O_WRONLY | O_APPEND | O_CREAT);

    // if (fd < 0) {
    // printf("Error opening file!\\n");
    // return -1;
    // }
    
    // if ({{ func_name }}({{ params }})) {
    // printf("There was an error writing to testfile.txt\\n");
    // return -1;
    // }
    
    {{ func_name }}({{ params }});
 
    return 0;
}
'''
# ex: python3.6 generator.py write 1 str:"ana are mere" 15
