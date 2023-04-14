bool* camelMatch(char ** queries, int queriesSize, char * pattern, int* returnSize){
    bool *res = (bool *)malloc(queriesSize*sizeof(bool));
    int lp=strlen(pattern);
    for (int i=0;i<queriesSize;++i){
        res[i]=true;
        int k=0;
        int lq=strlen(queries[i]);
        for(int j=0;j<lq;++j){
            if (k<lp && pattern[k]==queries[i][j]) ++k;
            else if (isupper(queries[i][j])) {res[i]=false;break;}
        }
        if (k<lp) res[i]=false;
    }
    *returnSize=queriesSize;
    return res;
}