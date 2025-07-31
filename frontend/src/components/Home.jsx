import React from 'react'
import './Home.css'

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Chào mừng đến với SmartTrip!</h1>
        <p>Khám phá, lên kế hoạch và tận hưởng chuyến du lịch tuyệt vời của bạn.</p>
      </header>
      <section className="home-features">
        <div className="feature-card">
          <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80" alt="Khám phá điểm đến" />
          <h2>Khám phá điểm đến</h2>
          <p>Tìm kiếm các địa điểm du lịch nổi tiếng, độc đáo và phù hợp với sở thích của bạn.</p>
        </div>
        <div className="feature-card">
          <img src="https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80" alt="Lên kế hoạch" />
          <h2>Lên kế hoạch dễ dàng</h2>
          <p>Tạo lịch trình, đặt vé máy bay, khách sạn và các dịch vụ khác chỉ với vài bước đơn giản.</p>
        </div>
        <div className="feature-card">
          <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=400&q=80" alt="Trải nghiệm tuyệt vời" />
          <h2>Trải nghiệm tuyệt vời</h2>
          <p>Chia sẻ hành trình, lưu giữ kỷ niệm và kết nối với cộng đồng đam mê du lịch.</p>
        </div>
      </section>
    </div>
  )
}

export default Home