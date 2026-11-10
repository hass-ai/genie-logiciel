import { ACCOUNT_LIST } from "./database.mjs";

export const accountDAO = {
  insertAccount(account) {
    ACCOUNT_LIST.push(account);
    console.log("BDD :",ACCOUNT_LIST);
  },
  retrieveAccountList() {
    let res=[];
    for (let a of ACCOUNT_LIST) {
      res.push({ id: a.id, lastName: a.lastName, firstName:a.firstName });
    }
    return res;
  },
  updateAccount(account) {
    for (let i=0; i<ACCOUNT_LIST.length; i++) {
      if (ACCOUNT_LIST[i].id===account.id) {
        ACCOUNT_LIST[i] = account;
      }
    }
    console.log("BDD :", ACCOUNT_LIST);
  },
  retrieveAccount(id) {
    for (let a of ACCOUNT_LIST) {
      if (a.id===id) {
        return { id: a.id, name: a.lastName+" "+a.firstName, creationDate: a.creationDate };
      }
    }
  },
};
