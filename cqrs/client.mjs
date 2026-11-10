import { accountCommand } from "./accountCommand.mjs";
import { accountQuery } from "./accountQuery.mjs";

let id1=accountCommand.addAccount("Dupont", "Jean");
accountCommand.addAccount("Martin","Lea");


console.log("liste :", accountQuery.getAccountList());

accountCommand.saveAccount(id1, "Dupont","Paul");

console.log("compte :",accountQuery.getAccount(id1));
