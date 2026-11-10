import { Account } from "./account.mjs";
import { accountCommandDAO } from "./accountCommandDAO.mjs";

export const accountCommand = {
  addAccount(lastName, firstName) {
    let account=new Account(undefined, lastName,firstName);
    accountCommandDAO.insertAccount(account);
    return account.id;
  },
  saveAccount(id,lastName, firstName) {
    let ancien = accountCommandDAO.findAccount(id);
    let account= new Account(id, lastName, firstName,ancien.creationDate);
    accountCommandDAO.updateAccount(account);
  },
};
