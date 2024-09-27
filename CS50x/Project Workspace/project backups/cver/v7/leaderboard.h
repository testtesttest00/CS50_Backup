bool record(int moves);
char *parse(char *pre);
bool printrank(void);
char *readcsv(char *line, int iter);

typedef struct node{
    char name[16];
    int moves;
    struct node *next;
} node;

int hash(int moves);
node *loadhash(int moves, char *name);
bool freehash(node *hashtable);
node *mergesort(node *linkedlist);
node *mergesort_merge(node *list1, node* list2);

node *stitchhash(int a, int b);
bool printtop(int places);
