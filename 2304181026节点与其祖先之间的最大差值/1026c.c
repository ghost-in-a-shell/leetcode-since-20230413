int diff(struct TreeNode* root,int maxval,int minval){
    int curres=abs(root->val-maxval)>abs(root->val-minval)? abs(root->val-maxval):abs(root->val-minval);
    int newmaxval=root->val>maxval? root->val:maxval;
    int newminval=root->val<minval? root->val:minval;
    if (root->left!=NULL){
        int leftres=diff(root->left,newmaxval,newminval);
        curres=curres>leftres? curres:leftres;
    }
    if (root->right!=NULL){
        int rightres=diff(root->right,newmaxval,newminval);
        curres=curres>rightres? curres:rightres;
    }
    return curres;
}
int maxAncestorDiff(struct TreeNode* root){
    return diff(root,root->val,root->val);
}
