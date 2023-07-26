package code1;

public class Member {
    private String id;
    private String name;
    private String email;
    private String password;
    private String phoneNum;
    private boolean sms_yn;

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setPhoneNum(String phoneNum) {
        this.phoneNum = phoneNum;
    }

    public void setSms_yn(boolean sms_yn) {
        this.sms_yn = sms_yn;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    public String getPhoneNum() {
        return phoneNum;
    }

    public boolean isSms_yn() {
        return sms_yn;
    }

    public String getId() {
        return id;
    }

}
