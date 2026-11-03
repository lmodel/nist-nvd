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
  A score under CVSS version 3.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV31  {

  private String version;
  private String vectorString;
  private String attackVector;
  private String attackComplexity;
  private String privilegesRequired;
  private String userInteraction;
  private String scope;
  private String confidentialityImpact;
  private String integrityImpact;
  private String availabilityImpact;
  private String exploitCodeMaturity;
  private String remediationLevel;
  private String reportConfidence;
  private Float temporalScore;
  private String temporalSeverity;
  private String confidentialityRequirement;
  private String integrityRequirement;
  private String availabilityRequirement;
  private String modifiedAttackVector;
  private String modifiedAttackComplexity;
  private String modifiedPrivilegesRequired;
  private String modifiedUserInteraction;
  private String modifiedScope;
  private String modifiedConfidentialityImpact;
  private String modifiedIntegrityImpact;
  private String modifiedAvailabilityImpact;
  private Float environmentalScore;
  private String environmentalSeverity;
  private float baseScore;
  private String baseSeverity;


}