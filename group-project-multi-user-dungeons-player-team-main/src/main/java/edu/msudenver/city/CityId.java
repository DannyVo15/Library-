package edu.msudenver.city;

import java.io.Serializable;

public class CityId implements Serializable {
    private String countryCode;
    private String postalCode;

    public CityId(String countryCode, String postalCode) {
        this.countryCode = countryCode;
        this.postalCode = postalCode;
    }

    public CityId() {
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }
}
