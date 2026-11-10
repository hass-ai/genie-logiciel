import { ACCOUNT_LIST } from "./database.mjs";

export const accountCommandDAO = {
  insertAccount(account) {
    ACCOUNT_LIST.push(account);
    console.log("BDD :",ACCOUNT_LIST);
  },
  updateAccount(account) {
    for (let i=0; i<ACCOUNT_LIST.length; i++) {
      if (ACCOUNT_LIST[i].id===account.id) {
        ACCOUNT_LIST[i] = account;
      }
    }
    console.log("BDD :", ACCOUNT_LIST);
  },
  findAccount(id) {
    for (let a of ACCOUNT_LIST) {
      if (a.id===id) {
        return a;
      }
    }
  },
};
