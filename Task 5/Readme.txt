📊 Global Superstore Business Dashboard

An interactive business intelligence dashboard built with Streamlit to analyze sales, profit, and customer performance using the Global Superstore dataset.

🔎 Features

Filters (Sidebar)

Region

Category

Sub-Category

KPIs

💰 Total Sales

📈 Total Profit

🏆 Top 5 Customers by Sales

Visualizations

Sales & Profit by Category

Top 5 Customers by Sales

Region-wise Sales

📂 Dataset

The dashboard uses the Global Superstore dataset (Global_Superstore.csv) which contains:

Customer Information: Customer Name, Segment, Region

Product Information: Category, Sub-Category, Product Name

Order Details: Sales, Profit, Quantity, Discount, Shipping Cost

Metadata: Order Date, Ship Date, Order ID

⚙️ Installation

Clone this repository and install dependencies:

git clone https://github.com/your-username/global-superstore-dashboard.git
cd global-superstore-dashboard
pip install -r requirements.txt


Or install dependencies manually:

pip install streamlit pandas matplotlib seaborn

🚀 Usage

Place the dataset file Global_Superstore.csv in the project folder.

Run the Streamlit app:

streamlit run app.py


The dashboard will open in your browser at: http://localhost:8501

📈 Example Insights

Identify top-performing regions by sales.

Discover which categories and sub-categories drive profit.

Find the top 5 customers contributing the most revenue.

Compare regional sales performance across business segments.

🛠️ Tech Stack

Python

Streamlit – dashboard UI

Pandas – data handling

Matplotlib & Seaborn – visualizations

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is open-source and available under the MIT License
.