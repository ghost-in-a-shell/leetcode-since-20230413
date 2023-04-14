int longestDecomposition(char * text){
    int res=1;
    int l= strlen(text);
    if (l==0) return 0;
    for(int i=0;i<l;++i){
        if (i>=l-i-1)      return 1;
        char * st1=(char*)malloc(i+2);
        char * st2=(char*)malloc(i+2);
        char * st3=(char*)malloc(l-2*i-1);
        memmove(st1,text,i+2);
        st1[i + 1] = '\0';
        strncpy(st2,text+l-i-1,i+1);
        st2[i + 1] = '\0';
        strncpy(st3,text+i+1,l-2*i-2);
        st3[l-2*i-2] = '\0';
        if (!strcmp(st1,st2)){
            free (st1);
            free (st2);
            return longestDecomposition(st3)+2;
            free (st3);
        }
        free (st1);
        free (st2);
        free (st3);
    }
    return 0xdeadbeef;
}