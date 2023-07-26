import java.sql.*;

public class DbTest {
    public void dbRead() {
        String url = "jdbc:mariadb://127.0.0.1:3306/test";
        String dbUserId = "root";
        String dbUserPassword = "alex2006";

        // db연결하기

        // ========== 1. 드라이버 로드 ==========
        try {
            Class.forName("org.mariadb.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("wrong");
            e.printStackTrace();
        }

        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet rs = null;


        // ========== 2. 커넥션 객체 생성 ==========
        try {
            connection = DriverManager.getConnection(url, dbUserId, dbUserPassword);

            // 3. ========== 스테이트먼트 객체 생성 ==========
            String sql = "select * from member ";


            // 4. ========== 쿼리 실행 ==========
            statement = connection.prepareStatement(sql);

            rs = statement.executeQuery();

            // ========== 5. 결과 수행 ==========
            while(rs.next()) {
                String name = rs.getString("name");
                String email = rs.getString("email");
                String phoneNum = rs.getString("phoneNum");
                String marketing_yn = rs.getString("marketing_yn");

                System.out.println(name + " " +  email + " " + phoneNum + " " + marketing_yn);
            }
        } catch (SQLException e) {
            System.out.println("wrong");
            e.printStackTrace();
        } finally {

            // ========== 6. 객체 연결 해제 ==========
            try {
                if (rs != null && !rs.isClosed()) rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (statement != null && !statement.isClosed()) statement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (connection != null && !connection.isClosed()) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public void dbInsert() {
        String url = "jdbc:mariadb://127.0.0.1:3306/test";
        String dbUserId = "root";
        String dbUserPassword = "alex2006";

        // db연결하기

        // ========== 1. 드라이버 로드 ==========
        try {
            Class.forName("org.mariadb.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("wrong");
            e.printStackTrace();
        }

        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet rs = null;

        String nameVal = "Joony";
        String emailVal = "Joony1@naver.com";
        String phoneNumVal = "01023142365";
        String passwordVal = "joony1";

        // ========== 2. 커넥션 객체 생성 ==========
        try {
            connection = DriverManager.getConnection(url, dbUserId, dbUserPassword);

            // 3. ========== 스테이트먼트 객체 생성 ==========
            String sql = "insert into member (name, email, phoneNum, password) " +
                    "values (?, ?, ?, ?)";

            // 4. ========== 쿼리 실행 ==========
            statement = connection.prepareStatement(sql);
            statement.setString(1, nameVal);
            statement.setString(2, emailVal);
            statement.setString(3, phoneNumVal);
            statement.setString(4, passwordVal);

            // 입력이 잘 되는지 결과값 나오도록 하기
            int affected = statement.executeUpdate();

            // ========== 5. 결과 수행 ==========
            if (affected > 0) System.out.println("success");
            else System.out.println("fail");

        } catch (SQLException e) {
            System.out.println("wrong");
            e.printStackTrace();
        } finally {

            // ========== 6. 객체 연결 해제 ==========
            try {
                if (rs != null && !rs.isClosed()) rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (statement != null && !statement.isClosed()) statement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (connection != null && !connection.isClosed()) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }


    public void dbUpdate() {
        String url = "jdbc:mariadb://127.0.0.1:3306/test";
        String dbUserId = "root";
        String dbUserPassword = "alex2006";

        // db연결하기

        // ========== 1. 드라이버 로드 ==========
        try {
            Class.forName("org.mariadb.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("wrong");
            e.printStackTrace();
        }

        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet rs = null;

        String nameVal = "Joony";
        String emailVal = "Joony1@naver.com";
        String phoneNumVal = "01023142365";
        String passwordVal = "joony1";

        // ========== 2. 커넥션 객체 생성 ==========
        try {
            connection = DriverManager.getConnection(url, dbUserId, dbUserPassword);

            // 3. ========== 스테이트먼트 객체 생성 ==========
            String sql = "update member set marketing_yn = true where name = ?";

            // 4. ========== 쿼리 실행 ==========
            statement = connection.prepareStatement(sql);
            statement.setString(1, nameVal);

            // 입력이 잘 되는지 결과값 나오도록 하기
            int affected = statement.executeUpdate();

            // ========== 5. 결과 수행 ==========
            if (affected > 0) System.out.println("success");
            else System.out.println("fail");

        } catch (SQLException e) {
            System.out.println("wrong");
            e.printStackTrace();
        } finally {

            // ========== 6. 객체 연결 해제 ==========
            try {
                if (rs != null && !rs.isClosed()) rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (statement != null && !statement.isClosed()) statement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (connection != null && !connection.isClosed()) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public void dbDelete() {
        String url = "jdbc:mariadb://127.0.0.1:3306/test";
        String dbUserId = "root";
        String dbUserPassword = "alex2006";

        // db연결하기

        // ========== 1. 드라이버 로드 ==========
        try {
            Class.forName("org.mariadb.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("wrong");
            e.printStackTrace();
        }

        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet rs = null;

        String nameVal = "Joony";
        String nameVal2 = "joon3@naver.com";

        // ========== 2. 커넥션 객체 생성 ==========
        try {
            connection = DriverManager.getConnection(url, dbUserId, dbUserPassword);

            // 3. ========== 스테이트먼트 객체 생성 ==========
            String sql = "delete from member" +
                    " where email = ?";

            // 4. ========== 쿼리 실행 ==========
            statement = connection.prepareStatement(sql);
            statement.setString(1, nameVal2);

            // 입력이 잘 되는지 결과값 나오도록 하기
            int affected = statement.executeUpdate();

            // ========== 5. 결과 수행 ==========
            if (affected > 0) System.out.println("success");
            else System.out.println("fail");

        } catch (SQLException e) {
            System.out.println("wrong");
            e.printStackTrace();
        } finally {

            // ========== 6. 객체 연결 해제 ==========
            try {
                if (rs != null && !rs.isClosed()) rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (statement != null && !statement.isClosed()) statement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (connection != null && !connection.isClosed()) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
