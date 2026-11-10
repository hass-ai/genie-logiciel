import { accountService } from "./accountService.mjs";

let id1=accountService.addAccount("Dupont", "Jean");
accountService.addAccount("Martin","Lea");


console.log("liste :", accountService.getAccountList());

accountService.saveAccount(id1, "Dupont","Paul");

console.log("compte :",accountService.getAccount(id1));
