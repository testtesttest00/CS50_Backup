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
