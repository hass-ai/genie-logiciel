import { Account } from "./account.mjs";
import { accountDAO } from "./accountDAO.mjs";

export const accountService = {
  addAccount(lastName, firstName) {
    let account=new Account(undefined, lastName,firstName);
    accountDAO.insertAccount(account);
    return account.id;
  },

  getAccountList() {
    return accountDAO.retrieveAccountList();
  },
  saveAccount(id,lastName, firstName) {
    let ancien = accountDAO.retrieveAccount(id);
    let account= new Account(id, lastName, firstName,ancien.creationDate);
    accountDAO.updateAccount(account);
  },
  getAccount(id) {
    return accountDAO.retrieveAccount(id);
  },
};
