package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A score under CVSS version 2.0, which has no severity bands.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV20  {

  private String version;
  private String vectorString;
  private float baseScore;
  private String confidentialityImpact;
  private String integrityImpact;
  private String availabilityImpact;
  private String remediationLevel;
  private String reportConfidence;
  private Float temporalScore;
  private String confidentialityRequirement;
  private String integrityRequirement;
  private String availabilityRequirement;
  private Float environmentalScore;
  private String accessVector;
  private String accessComplexity;
  private String authentication;
  private String exploitability;
  private String collateralDamagePotential;
  private String targetDistribution;


}