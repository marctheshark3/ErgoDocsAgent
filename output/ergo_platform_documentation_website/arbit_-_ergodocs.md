# Arbit - ErgoDocs
Source: [https://docs.ergoplatform.com/uses/arbit/](https://docs.ergoplatform.com/uses/arbit/)
Generated: 2025-05-11

## Summary
Arbit is a simple and intuitive arbitrage platform designed for decentralized trading on the Ergo and Cardano blockchains. It aims to simplify the arbitrage process, enabling users to identify and execute profitable swaps with minimal setup. This project is a work in progress and is not yet ready for production use. What is Arbit? Arbit streamlines the process of arbitrage trading by providing a clean and simple interface.

## Keywords
arbit, arbitrage, platform, trading, ergo, cardano, blockchain, process, user, swap, setup, project, work, progress, production, interface, opportunity, token, exchange, profit

## Content
## Arbit Documentation#
Arbit is a simple and intuitive arbitrage platform designed for decentralized trading on the Ergo and Cardano blockchains. It aims to simplify the arbitrage process, enabling users to identify and execute profitable swaps with minimal setup.
WIP
This project is a work in progress and is not yet ready for production use.

### Overview#
What is Arbit?
Arbit streamlines the process of arbitrage trading by providing a clean and simple interface. The platform identifies opportunities where a user can buy and sell tokens across different decentralized exchanges to make a profit.
Supported Tokens: ERG, ADA, and RSN.
Supported Exchanges: Ergo Dex and Splash.

Core Features:

Predefined arbitrage strategies (called "Arbits").
Focus on simplicity and usability.
Execution of swaps with just a few clicks.
What is an Arbit?
An Arbit is a series of swaps that generate profit. For example:
Sell 100 X tokens on Exchange A for $100.
Buy 105 Y tokens on Exchange B for the same $100.
Profit from the additional 5 Y tokens.

#### Simplicity and Usability#
Designed for users with basic blockchain knowledge.
Clear interface with no distractions or unnecessary complexity.
Profitability of swaps displayed prominently.

#### Fixed Arbitrage Strategies#
Supports predefined arbitrage paths, such as:

ERG â ADA
RSN â ADA



Profit calculations are based on fixed USD values ($50 and $100).

### How It Works#
Arbitrage Strategy Execution:

Predefined paths calculate profitability based on current market conditions.
Fixed token values ($50 and $100) are used for calculations to avoid complexity.



Supported Providers:

Ergo Dex: Facilitates ERG and ADA swaps.
Splash: Enables swapping of RSN and ADA tokens.



Profit Calculation:

Example for a $50 swap:
Sell $50 worth of rsADA on Ergo Dex for ERG.
Swap ERG for ADA on Splash.
Compare the ADA received with the initial $50 equivalent.

#### Local Setup#
Clone the Repository:
git clone https://github.com/ConnecMent/arbit.git
cd arbit



Set Up Environment Variables:
Create a .env file in the root directory with the following variables:

SPLASH_API_URL: API URL for Splash exchange.
ERGO_EXPLORER_API_URL: API URL for Ergo Explorer.

Example:
SPLASH_API_URL=https://api.splash.exchange
ERGO_EXPLORER_API_URL=https://api.ergoplatform.com



Run the Development Server:
Install dependencies and start the development server:
pnpm install
pnpm run dev

The application will be available at http://localhost:3000.

### Arbitrage Strategies#
The following strategies are implemented in Arbit:

#### ERG â ADA Arbitrage#
Leverages Ergo Dex and Splash to identify profitable swaps between ERG and ADA.
Calculations consider both direct and reverse swap paths for maximum opportunities.

#### RSN â ADA Arbitrage#
Utilizes Ergo Dex and Splash for swaps between RSN and ADA tokens.
Similar profit calculation methods as the ERG â ADA strategy.

#### Core Arbitrage Logic#
The core logic for arbitrage is implemented in src/arbitrategy.ts. It defines a set of predefined strategies for swapping between supported tokens and providers.

#### Provider Integrations#
Ergo Dex (src/providers/ergodex.ts):

Interacts with the Ergo Dex SDK for swapping tokens.
Supports x2y and y2x operations.



Splash (src/providers/splash.ts):


Uses the Splash API to fetch order book data.

Supports bid/ask matching for liquidity and price calculations.

### Usage Guide#
Prepare Tokens:

Ensure you have supported tokens (ERG, ADA, RSN) on Ergo and Cardano chains.
Use Rosen Bridge to bridge assets if necessary.



Visit the App:

Open the application and review the displayed arbitrage opportunities.



Execute a Swap:

If a profitable Arbit is available, execute the swap by following the on-screen instructions.

### Contributing#
The project is maintained by ConnecMent. Contributions are welcome via pull requests.
Team:
Mentors: @mkermani144, @fatemeh-ra
Mentee: @SeyedMojtaba1
Special thanks to @zargarzadehm for Ergo Dex SDK insights.
