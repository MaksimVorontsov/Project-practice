#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *get_str_from_file(char *file){
    FILE *fp;
    char *res = NULL;
    printf("%s\n", file);
    if((fp=fopen(file, "rb"))==NULL) {
        printf ("Cannot open file.\n");
    }
    else{
        int end = 0;
        int len = 0;
        while (end == 0) {
            char *buf = NULL;
            int buf_size = 3;
            buf = calloc(buf_size, sizeof(char));
            int read_size = fread(buf, sizeof(char), buf_size, fp);
            int len1 = len;
            len = len + read_size;
            res = realloc(res, (len + 1)*sizeof(char));
            memcpy(res + len1, buf, read_size);
            *(res + len) = '\0';
            free(buf);
            if (feof(fp)) {
                end = 1;
                printf("Premature end of file.\n");
            }
        }
        fclose(fp);
    }
    return res;
}
char *get_str() {
    char buf[81] = {0};
    char *res = NULL;
    int len = 0;
    int n;
    do {
        n = scanf("%80[^\n]", buf);
        if (n < 0) {
            if (!res) {
                return NULL;
            }
        } else if (n > 0) {
            int chunk_len = (int) strlen(buf);
            int str_len = len + chunk_len;
            res = realloc(res, str_len + 1);
            memcpy(res + len, buf, chunk_len);
            len = str_len;
        } else {
            scanf("%*c");
        }
    } while (n > 0);

    if (len > 0) {
        res[len] = '\0';
    } else {
        res = calloc(1, sizeof(char));
    }

    return res;
}
int chek_if_int(char *p){
    int n = (int) strlen(p);
    for (int i = 0; i < n; i++) {
        if (*(p + i) < 58 && *(p + i) > 47);
        else{
            if (i == 0 && *p == 45)
                ;
            else
                return 1;
        }
    }
    return 0;
}
int expon(int x, int n)
{
    int count;
    int i = 0;
    count = 1;
    while ( i < n){
        count = count * x;
        i++;
    }
    return count;
}
int str_to_int(char *p){
    int sum = 0;
    int add;
    int neg = 0;
    if (*p == '-'){
        neg = 1;
    }
    int n = (int)strlen(p);
    for (int i = 0; i < n - neg; i++){
        add = (p[n -1 - i] - '0')*expon(10, i);
        sum += add;
    }
    if (neg == 1){
        sum = -1 * sum;
    }
    return sum;
}
void dividebynum(char *in, int *out){
    char *buf = NULL;
    int i = 0;
    int j = 0;
    int counter = 0;
    while (i < strlen(in)){
        while (in[j] != ' ' || j != strlen(in)){
            counter += 1;
            j++;
        }
        i+= j;
        j = 0;

        counter  = 0
    }
}
int chek(char *p, int *d){
    p = get_str();
    if (p){
        int n = chek_if_int(p);
        if (n == 0){
            int m = str_to_int(p);
            *d = m;
            free(p);
            return 0;
        }
        else
            free(p);
            printf("Please chek your inputs\n");
        return 1;
    }
    free(p);
    return 1;
}
void print(int *p, int m){
    printf("array:\n");
    int i;
    for (i = 0; i < m; i++){
        printf("%d ", p[i]);
    }
    printf("\n");
    if (i == 0)
        printf("No data\n");
}
void swap(int *d1, int *d2) {
    int tmp = *d1;
    *d1 = *d2;
    *d2 = tmp;
}
void array_sort(int *data, int len) {
    for (int i = 0; i < len - 1; ++i) {
        for (int j = 0; j < len - i - 1; ++j) {
            if (data[j] > data[j + 1]) {
                swap(&data[j], &data[j + 1]);
            }
        }
    }
}
int main() {
    int maincounter = 0;

    int *step1;
    int n1;
    step1 = &n1;
    int m1;

    int lengthofarray = 0;
    int min = -1000;
    int max = 1000;

    int *array = NULL;

    while (maincounter == 0) {
        printf("Choose your option:\n1 - Fill data from keyboard\n2 - Fill data from file\n3 - Randomize data\n4 - Print data\n5 - Sort data\n6 - Exit\n");
        char *s = NULL;
        m1 = chek(s, step1);
        if (m1 == 0) {
            if (n1 == 1) {
                printf("Input the amount of numbers\n");
                int *step2;
                int n2;
                int m2;
                step2 = &n2;
                char *p = NULL;
                m2 = chek(p, step2);
                if (m2 == 0 && n2 > 0) {
                    lengthofarray = n2;
                    array = realloc(array, n2*sizeof(int));
                    printf("Input integer:\n");
                    for (int i = 0; i < n2; i++) {
                        int wrong = 0;
                        while (wrong == 0) {
                            printf("Number - %d out of %d:\n", i+1, n2 );
                            char *v = NULL;
                            int *step3;
                            int n3;
                            int m3;
                            step3 = &n3;
                            m3 = chek(v, step3);
                            if (m3 == 0) {
                                *(array + i) = n3;
                                wrong = 1;
                            }
                            else;
                            }
                    }
                }
                else;
            }
            else if (n1 == 2){
                char name[] = "C:\\Users\\Rachu\\CLionProjects\\Lab4\\test.txt";
                char *pos = NULL;
                pos = get_str_from_file(name);
                int counter = 0;
                for(int i = 0; i < strlen(pos) ; i++){
                    if ( (pos[i]=='\n') || (pos[i]==' ') || (pos[i]=='\t') || ((int)pos[i] == 13))
                        *(pos+i) = ' ';
                    else if (pos[i] <= '9' && pos[i] >= '0')
                        counter +=1;
                    else if (pos[i]=='-' && i != strlen(pos)){
                        if (i != 0 && pos[i-1] != ' ' || !(pos[i+1] <= '9' && pos[i+1] >= '0')) {
                            counter = -1;
                            break;
                        }
                        else counter += 1;
                    }
                    else {
                        counter = -1;
                        break;
                    }
                }
                printf("Result:<<%s>>\n", pos);
                if (counter == -1) {
                    printf("File data is incorrect. Please chek it.\n");
                    free(pos);
                }
                else {
                    int todelete = 0;
                    for (int i = 0; i < strlen(pos); i++) {
                        if (pos[i] == ' ' && (i == 0 || i == strlen(pos)) || (i != strlen(pos) && pos[i] == ' ' && pos[i + 1] == ' ')) {
                            todelete += 1;
                        }
                    }
                    char *ollo = NULL;
                    int length = strlen(pos) - todelete;
                    ollo = calloc(length + 1, sizeof(char));
                    printf("%d - %d\n", todelete, length);
                    int j = 0;
                    for (int i = 0; i < strlen(pos); i++) {
                        if ((pos[i] == ' ' && (i == 0 || i == strlen(pos))) || (i != strlen(pos) && pos[i] == ' ' && pos[i + 1] == ' '));
                        else {
                            *(ollo + j) = pos[i];
                            j++;
                        }
                    }
                    *(ollo + length) = '\0';
                    printf("Result:<<%s>>\n", ollo);
                    free(pos);

                    free(ollo);
                }

            }
            else if (n1 == 3){
                printf("Enter number of elements:\n");
                char *v2 = NULL;
                int *step5;
                int n5;
                int m5;
                step5 = &n5;
                m5 = chek(v2, step5);
                if (m5 == 0){
                    array = realloc(array, n5 *sizeof(int));
                    for (int i = 0; i < n5; ++i) {
                        int t = rand() % 2;
                        printf("t = %d\n", t);
                        array[i] = expon(-1, t)*(rand() % 1000);
                    }
                    lengthofarray = n5;
                }
            }
            else if (n1 == 4){
                print(array, lengthofarray);
            }
            else if (n1 == 5){
                //Choose interval
                for (int i = 0; i < 2; i++) {
                    int wrong1 = 0;
                    while (wrong1 == 0) {
                        if (i == 0)
                            printf("Input the minimum:\n" );
                        else if (i == 1)
                            printf("Input the maximum:\n" );
                        char *v1 = NULL;
                        int *step4;
                        int n4;
                        int m4;
                        step4 = &n4;
                        m4 = chek(v1, step4);
                        if (m4 == 0) {
                            if (i == 0)
                                min = n4;
                            if (i == 1)
                                max = n4;
                            wrong1 = 1;
                        }
                    }
                }
                if (max < min){
                    int temp = max;
                    max = min;
                    min = temp;
                }
                printf("min = %d and max = %d\n", min, max);
                //end of choosing
                int ininterval = 0;
                for (int i = 0; i < lengthofarray; i++){
                    if (array[i] >= min && array[i] <= max)
                        ininterval++;
                }
                int lengthofnewray = lengthofarray - ininterval;
                int *newray = NULL;
                newray = calloc(lengthofnewray, sizeof(int));
                int j = 0;
                for (int i = 0; i < lengthofarray; i++){
                    if (array[i] >= min && array[i] <= max);
                    else{
                        *(newray + j) = array[i];
                        j++;
                    }
                }
                array_sort(newray, lengthofnewray);
                printf("Before:\n");
                for (int i = 0; i < lengthofarray; i++)
                    printf("%d ", array[i]);
                printf("\n");
                printf("After:\n");
                for(int i = 0; i < lengthofnewray; i++)
                    printf("%d ", newray[i]);
                printf("\n");
                printf("Amount of Deleted = %d\n", ininterval);
                free(newray);
            }
            else if (n1 == 6) {
                maincounter = 1;
            }
            else
                printf("Please input correct number\n");
        } else;
    }
    free(array);
    }

