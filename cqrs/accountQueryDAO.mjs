import { ACCOUNT_LIST } from "./database.mjs";
import { accountSummaryList } from "./queryDatabase.mjs";

export const accountQueryDAO = {
  retrieveAccountList() {
    let res=[];
    for (let a of accountSummaryList) {
      res.push({ id: a.id, lastName: a.lastName, firstName:a.firstName });
    }
    return res;
  },
  retrieveAccount(id) {
    for (let a of ACCOUNT_LIST) {
      if (a.id===id) {
        return { id: a.id, name: a.lastName+" "+a.firstName, creationDate: a.creationDate };
      }
    }
  },
};
