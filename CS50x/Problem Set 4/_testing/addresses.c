#include <stdio.h>
#include <cs50.h>

int main(void){
    int x = 12;
    int *p = &x;
    //int *p2 = x;

    printf("\nint memory\n");
    printf("*p   %p\n", p);
    printf("&x   %p\n", &x);

    string s = "test";
    //string s2 = *s;
    char *s2 = s;
    //char *s3 = &s; cant as s alr has hidden & (x needs &x to be &p, whereas s can be printed as %p directly)
    //int *p2 = &s;
    char *s3 = "test"; //can be used without #include <cs50.h> header file
    //char *s4 = &"test"; "" acts as &
    printf("\nstring memory\n");
    printf("      &s %p\n", &s);
    printf("     *&s %s\n", *&s);
    printf("       s %p\n", s);
    printf("   &s[0] %p\n", &s[0]);
    printf("  *&s[0] %c\n", *&s[0]);
    printf("      *s %c\n", *s);
    printf("*&char*s %s\n", *&(s2));
    printf(" &char*s %p\n", &(s2));
    //printf("s2(s*) %p\n", s2);
    //printf("p2(&s) %p\n", p2);
    printf("  char*s %p\n", s2);
    printf(" *char*s %c\n", *s2);
    printf(" &char*s %p\n", &s2);
    //printf(" char*&s %p\n", s3)
    printf("  char*s %p\n", s3);
    printf("  char*s %s\n", s3);
    //printf("  char*s %c\n", s4);
    printf("  char*s %c\n", *s3);
    printf("   &test %p\n", &"test");
    printf("   *test %c\n", *"test");
    printf("  *&test %s\n", *&"test");
}

//                       type   output
// int x = 50      >>>   %i     50
// int *p = &x     >>>   %p     0xf(x = 50)
// &x              >>>   %p     0xf(x = 50)
// prt(*p | *&x)   >>>   %i     50
//--------------------------------------------
// string s = test >>>   %s     test
//
// char *p = s     >>>   %p     0xf(s[0] = t) (char *p = &s is wrong, take it that its already &s, allowing prt(s))
// prt(*p)         >>>   %c     t
// prt(s)          >>>   %p     0xf(s[0] = t) (only prt giving memory location)
// prt(*s)         >>>   %c     t
// &s[0]           >>>   %p     0xf(s[0] = t)
// prt(*&s[0])     >>>   %c     t
//
// &"test"         >>>   %p     0xf(s[0] = t)
// prt(*&"test")   >>>   %s     test
// prt(%s, 0xf(s)) >>>   %s     test (string type is represented by the location of a char array. %s <- 0xf(t) outputs test)
// prt(*"test")    >>>   %c     t (string represented by s[0], *s[0] is a char)
// prt(%c,*0xf(s)) >>>   %c     t (summarises above examples)
//
// &s              >>>   %p     0xf(???) (very far away from prt(s))
// prt(*&s)        >>>   %s     test
// &p              >>>   %p     0xf(???) (somehow location is -8 from &s ??)
// prt(*&p = s)    >>>   %s     test
