
import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard endpoint:', endpoint);
        console.log('Fetched leaderboard:', data);
        setLeaders(data.results || data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div>
      <h2 className="mb-4">Leaderboard</h2>

      {/* Bootstrap Card */}
      <div className="card mb-4">
        <div className="card-body">
          <h5 className="card-title">Leaderboard</h5>
          <p className="card-text">Top users and teams in Octofit Tracker.</p>
          <button className="btn btn-primary mb-3" onClick={() => setShowModal(true)}>Show Modal</button>

          {/* Bootstrap Table */}
          <table className="table table-striped">
            <thead>
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Score</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              {leaders.map((leader, idx) => (
                <tr key={leader.id || idx}>
                  <td>{leader.id || idx + 1}</td>
                  <td>{leader.name || 'N/A'}</td>
                  <td>{leader.score || 'N/A'}</td>
                  <td><button className="btn btn-link">View</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Bootstrap Form */}
      <form className="mb-4">
        <div className="mb-3">
          <label htmlFor="leaderName" className="form-label">Leader Name</label>
          <input type="text" className="form-control" id="leaderName" placeholder="Enter leader name" />
        </div>
        <button type="submit" className="btn btn-success">Add Leader</button>
      </form>

      {/* Bootstrap Modal */}
      {showModal && (
        <div className="modal show d-block" tabIndex="-1" role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Leaderboard Modal</h5>
                <button type="button" className="btn-close" aria-label="Close" onClick={() => setShowModal(false)}></button>
              </div>
              <div className="modal-body">
                <p>This is a Bootstrap modal example for leaderboard.</p>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>Close</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Leaderboard;
