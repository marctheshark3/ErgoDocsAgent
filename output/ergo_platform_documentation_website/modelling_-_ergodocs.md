# Modelling - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/data-model/box/box_modeling/](https://docs.ergoplatform.com/dev/data-model/box/box_modeling/)
Generated: 2025-05-11

## Summary
(Back to: Box Overview | Registers) The UTXO (Unspent Transaction Output) system is the backbone of many blockchain networks, and at its core are boxes. These boxes are not just containers for the value of a currency within a blockchain; they are also equipped with registers that are protected by a contract, enhancing their functionality on the Ergo blockchain. Registers are essentially storage units for data and information at specific addresses in the blockchain. To visualize this, think of these boxes as advanced storage units or containers.

## Keywords
overview, registers, utxo, unspent, transaction, output, system, backbone, network, core, container, value, currency, blockchain, register, contract, functionality, ergo, storage, unit

## Content
## Ergo Box Design: A Comprehensive Guide#
(Back to: Box Overview | Registers)
The UTXO (Unspent Transaction Output) system is the backbone of many blockchain networks, and at its core are boxes. These boxes are not just containers for the value of a currency within a blockchain; they are also equipped with registers that are protected by a contract, enhancing their functionality on the Ergo blockchain.
Registers are essentially storage units for data and information at specific addresses in the blockchain. To visualize this, think of these boxes as advanced storage units or containers. For instance, consider a cup:
A Cup:
Holds liquid primarily
Can contain a certain quantity of liquid
Now, let's translate this into a blockchain context:
A Cup Box:
Stores only Ergs or a specific token
Has a storage limit enforced by a guard script
A guard script or smart contract sets restrictions on the box. Without it, a box is just a storage unit for information or a certain amount of currency. The introduction of guard scripts, which establish specific rules for the boxes, adds a level of control and functionality to the boxes, much like a remote control. The focus here is not on the internal workings of a remote control (guard script) or the data it transmits (registers and storage), but on its functionality - pressing a button changes the TV channel.

### Understanding Box Modeling#
Box modeling is a framework that aids developers or box designers in creating a box to perform specific tasks. This structure promotes a clear and systematic understanding of a box's roles and operational mechanics.

### Key Principles in Box Design#
A blockchain serves as a financial canvas, allowing developers, engineers, and designers to build financial systems on top of it. However, design flaws can lead to security vulnerabilities, unscalable designs, and inefficient processes. Therefore, it's crucial to prioritize security, scalability, and efficiency in design.
The three pillars of box design are:

#### Security#
The box should be designed to prevent exploitation by unauthorized users. Its protection script must be robust.

#### Scalability#
The system (involving potentially many boxes and transactions) should be designed to handle multiple concurrent requests smoothly without causing congestion or excessive fees.

#### Efficiency#
A straightforward design makes it easier for engineers to understand, audit, and improve the design, reducing the chance of errors.

### Box Modeling: A Step-by-Step Guide#
Before diving into the principles mentioned above, it's essential to understand the basics of box modeling.
When modeling a box, consider the following:

#### What is the box's purpose?#
For instance, a lending box is designed to simplify the loan process within a DeFi application.

#### What data should the box store?#
The box's function determines the data stored in its registers. A lending box, for example, would store lending-related information (like loan amount, interest rate, collateral details, borrower/lender addresses) in its registers (R4-R9).

#### How will the box perform its function?#
This step involves thinking about the overall transaction flow, not just the individual box. It requires scripting the guard script (using ErgoScript) to enforce the rules and perform its intended function using the data stored in the registers and potentially data from other input boxes or data inputs.

#### Register Data Types#
Registers can store data in various formats, which can be single or multiple entries. See the Registers page for a list of supported types like Long, Coll[Byte], GroupElement, etc.

### Resources#
This guide is based on the article by Keith Lim
For more technical details on how boxes are represented in transactions, see the Transaction Format page.
